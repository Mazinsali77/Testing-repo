# -*- coding: utf-8 -*-

import logging
import random

from odoo import http, fields
from odoo.http import request
from datetime import datetime, timedelta
from collections import defaultdict
logger = logging.getLogger(__name__)

class IgniteDashboard(http.Controller):
    @http.route(['/ignite_dashboard/order'], type='http', auth='public')
    def make_order(self):
        """
        Renders the public page to make orders
        """
        return request.render('ignite_dashboard.order_public_page')

    @http.route(['/ignite_dashboard/validate_order'], type='http', auth="public", methods=['POST'], website=True)
    def validate_order(self, name, email, address, quantity, size, url):
        """
        Creates an order (and optionally a partner) with the given data
        """
        Partner = request.env['res.partner'].sudo()
        customer = Partner.search([('email', '=', email)], limit=1)
        if not customer:
            customer = Partner.create({
                'street': address,
                'email': email,
                'name': name,
            })
        request.env['ignite_dashboard.order'].create({
            'customer_id': customer.id,
            'quantity': quantity,
            'size': size,
            'image_url': url,
        })
        return request.render('ignite_dashboard.thank_you')

    @http.route('/ignite_dashboard/sale/statistics', type='json', auth='user')
    def get_sale_statistics(self):
        SaleOrder = http.request.env['sale.order']
        sale_quotations = SaleOrder.search_count([('state', '=', 'draft')])
        sale_orders = SaleOrder.search_count([('state', 'in', ['sale', 'done'])])
        sale_revenue = sum(order.amount_total for order in SaleOrder.search([('state', 'in', ['sale', 'done'])]))
        sale_average_order = round(sale_revenue / sale_orders, 2) if sale_orders else 0
        
        # Filter for the last three months
        three_months_ago = fields.Date.to_string(datetime.today() - timedelta(days=90))
        sales_last_three_months = SaleOrder.search([('date_order', '>=', three_months_ago), ('state', 'in', ['sale', 'done'])])
        # Filtering records for the last three months
        recent_sales_orders = SaleOrder.search([('date_order', '>=', three_months_ago)])
        recent_quotations = SaleOrder.search([('date_order', '>=', three_months_ago), ('state', '=', 'draft')])

        # Group by month and calculate sales
        monthly_sales = {}
        for order in sales_last_three_months:
            month = order.date_order.strftime("%B %Y")
            monthly_sales[month] = monthly_sales.get(month, 0) + order.amount_total

        # Top Quotations
        top_quotations = recent_quotations.sorted(key=lambda r: r.amount_total, reverse=True)[:5]

        # Top Sales Orders
        top_sales_orders = recent_sales_orders.sorted(key=lambda r: r.amount_total, reverse=True)[:5]

        # Top Products
        product_category_totals = defaultdict(float)
        sales_rep_totals = defaultdict(float)
        customer_purchase_frequency = defaultdict(int)

        SaleOrderLine = http.request.env['sale.order.line']
        recent_lines = SaleOrderLine.search([('order_id', 'in', recent_sales_orders.ids)])
        product_totals = {}
        for line in recent_lines:
            product_totals[line.product_id] = product_totals.get(line.product_id, 0) + line.product_uom_qty
            category = line.product_id.categ_id
            product_category_totals[category] += line.price_subtotal

        top_products = sorted(product_totals.items(), key=lambda x: x[1], reverse=True)[:5]

        # Top Customers
        customer_totals = {}
        for order in recent_sales_orders:
            customer_totals[order.partner_id] = customer_totals.get(order.partner_id, 0) + order.amount_total
            sales_rep = order.user_id
            sales_rep_totals[sales_rep] += order.amount_total
            customer = order.partner_id
            customer_purchase_frequency[customer] += 1

        top_customers = sorted(customer_totals.items(), key=lambda x: x[1], reverse=True)[:5]

        category_sales_distribution = {}
        sales_rep_performance = {}
        customer_frequency_chart = {}

        for cat, total in product_category_totals.items():
            category_sales_distribution[cat.name] = total
        for rep, total in sales_rep_totals.items():
            sales_rep_performance[rep.name] = total
        for cust, count in customer_purchase_frequency.items():
            customer_frequency_chart[cust.name] = count

        # category_sales_distribution = [{cat.name : total} for cat, total in product_category_totals.items()]
        # sales_rep_performance = [{rep.name: total} for rep, total in sales_rep_totals.items()]
        # customer_frequency_chart = [{cust.name: count} for cust, count in customer_purchase_frequency.items()]
         
        

        return {
            'sale_quotations': sale_quotations,
            'sale_orders': sale_orders,
            'sale_revenue': sale_revenue,
            'sale_average_order': sale_average_order,
            'monthly_sales': monthly_sales,
            'top_quotations': [(q.name, q.amount_total) for q in top_quotations],
            'top_sales_orders': [(so.name, so.amount_total) for so in top_sales_orders],
            'top_products': [(p.id, p.name, qty) for p, qty in top_products],
            'top_customers': [(c.id, c.name, total) for c, total in top_customers],
            'category_sales_distribution': category_sales_distribution,
            'sales_rep_performance': sales_rep_performance,
            'customer_frequency_chart': customer_frequency_chart,
        }
    
    @http.route('/ignite_dashboard/purchase/statistics', type='json', auth='user')
    def get_purchase_statistics(self):
        PurchaseOrder = http.request.env['purchase.order']
        PurchaseOrderLine = http.request.env['purchase.order.line']
        three_months_ago = fields.Date.to_string(datetime.today() - timedelta(days=90))
        purchase_purchased = PurchaseOrder.search_count([('date_order', '>=', three_months_ago), ('state', '=', 'purchase')])
        purchase_orders_obj = PurchaseOrder.search([('date_order', '>=', three_months_ago), ('state', 'in', ['purchase', 'done'])])
        purchase_orders = PurchaseOrder.search_count([('date_order', '>=', three_months_ago), ('state', 'in', ['purchase', 'done'])])
        purchase_orders_count = purchase_orders
        purchase_total = sum(order.amount_total for order in PurchaseOrder.search([]))
        purchase_average_order = purchase_total / purchase_orders if purchase_orders else 0
        # Calculate Lead Time for each order
        total_lead_time = 0
        count = 0

        for order in purchase_orders_obj:
            if order.date_order and order.date_approve:
                lead_time = (order.date_approve - order.date_order).days
                total_lead_time += lead_time
                count += 1

        # Average Lead Time to Receive
        average_lead_time = total_lead_time / count if count > 0 else 0

        # purchase_lead_time_to_receive = sum(order.lead_time_to_receive for order in PurchaseOrder.search([])) / purchase_orders if purchase_orders else 0
        monthly_purchases = defaultdict(float)
        purchase_orders = PurchaseOrder.search([('date_order', '>=', three_months_ago), ('state', 'in', ['purchase', 'done'])])
        for order in purchase_orders:
            month = order.date_order.strftime("%B %Y")
            monthly_purchases[month] += order.amount_total
        
        purchase_lines = PurchaseOrderLine.search([('order_id', 'in', purchase_orders.ids)])
        product_quantities = defaultdict(float)
        for line in purchase_lines:
            product_quantities[line.product_id] += line.product_qty

        top_products = sorted(product_quantities.items(), key=lambda x: x[1], reverse=True)[:5]


        vendor_totals = defaultdict(float)
        for order in purchase_orders:
            vendor_totals[order.partner_id] += order.amount_total

        top_vendors = sorted(vendor_totals.items(), key=lambda x: x[1], reverse=True)[:5]


        vendor_totals = defaultdict(float)
        for order in purchase_orders:
            vendor_totals[order.partner_id] += order.amount_total

        top_vendors = sorted(vendor_totals.items(), key=lambda x: x[1], reverse=True)[:5]
        
        status_distribution = defaultdict(int)
        for order in purchase_orders:
            status_distribution[order.state] += 1



        top_purchased_products = {}
        for prod, qty in top_products:
            top_purchased_products[prod.name] = qty
        vendor_performance = {}
        for ven, total in top_vendors:
            vendor_performance[ven.name] = total

        
        
        return {
            'purchase_purchased': purchase_purchased,
            'purchase_orders': purchase_orders_count,
            'purchase_average_order': purchase_average_order,
            'purchase_lead_time_to_receive': (str(int(average_lead_time)) + ' days') or '0 days',
            'monthly_purchases': dict(monthly_purchases),
            'top_purchased_products': top_purchased_products,
            'vendor_performance': vendor_performance,
            'purchase_order_status_distribution': dict(status_distribution),
        }
    
    @http.route('/ignite_dashboard/inventory/statistics', type='json', auth='user')
    def get_inventory_statistics(self):
        Product = http.request.env['product.product']
        products = Product.search([])
        inventory_value = sum(product.qty_available * product.standard_price for product in products)

        category_values = defaultdict(float)
        for product in products:
            category = product.categ_id
            category_values[category] += product.qty_available * product.standard_price

        product_stock_values = [(product, product.qty_available * product.standard_price) for product in products]
        top_product_stock_levels = sorted(product_stock_values, key=lambda x: x[1], reverse=True)[:5]

        inventory_value_by_category = {}
        stock_levels_top_products = {}
        
        for cat, value in category_values.items():
            inventory_value_by_category[cat.name] = value
        for prod, value in top_product_stock_levels:
            stock_levels_top_products[prod.name] = value

        logger.info("new_data")
        logger.info(inventory_value_by_category)
        logger.info(stock_levels_top_products)

        return {
            'inventory_value': inventory_value,
            'inventory_value_by_category': inventory_value_by_category,
            'stock_levels_top_products': stock_levels_top_products,
        }
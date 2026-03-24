/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Layout } from "@web/search/layout";
import { getDefaultConfig } from "@web/views/view";
import { useService } from "@web/core/utils/hooks";
import { Domain } from "@web/core/domain";
import { Notebook } from "@web/core/notebook/notebook";
import { Card } from "./card";
const { Component, useSubEnv, onWillStart } = owl;
import { PieChart } from "./pie_chart";
import { LineChart } from "./line_chart";
import { DoughnutChart } from "./doughnut_chart";
import { BarChart } from "./bar_chart";

class IgniteDashboard extends Component {
    setup() {
        
        // The useSubEnv below can be deleted if you're > 16.0
        useSubEnv({
            config: {
                ...getDefaultConfig(),
                ...this.env.config,
            },
        });

        this.display = {
            controlPanel: { "top-right": false, "bottom-right": false },
        };

        this.action = useService("action");
        this.igniteService = useService("igniteService");

        this.saleKeyToString = {
            sale_quotations: "Quotations",
            sale_orders: "Orders",
            sale_revenue: "Revenue",
            sale_average_order: "Average Order",
        };
        this.purchaseKeyToString = {
            purchase_purchased: "Purchased",
            purchase_orders: "Orders",
            purchase_average_order: "Average Order",
            purchase_lead_time_to_receive: "Lead Time to Receive",
        };
        this.inventoryKeyToString = {
            inventory_value: "Inventory Value",
        };
        onWillStart(async () => {
            this.saleStatistics = await this.igniteService.loadSaleStatistics();
            this.purchaseStatistics = await this.igniteService.loadPurchaseStatistics();
            this.inventoryStatistics = await this.igniteService.loadInventoryStatistics();
        });

        
    }
    openSettings() {
        this.action.doAction("base_setup.action_general_configuration");
    }
    openCustomerView() {
        this.action.doAction("base.action_partner_form");
    }
    openContactsView() {
        this.action.doAction("base.action_partner_form");
    }
    openDashboardsView() {
        this.action.doAction("spreadsheet_dashboard.ir_actions_dashboard_action");
    }
    openUsersView() {
        this.action.doAction("base.action_res_users");
    }
    openGroupsView() {
        this.action.doAction("base.action_res_groups");
    }
    openCompaniesView() {
        this.action.doAction("base.action_res_company_form");
    }
    openAppsView() {
        this.action.doAction("base.open_module_tree");
    }
    openCalendarView() {
        this.action.doAction("calendar.action_calendar_event");
    }
    openDiscussView() {
        this.action.doAction("mail.action_discuss");
    }
    openPipelineView() {
        this.action.doAction("crm.crm_lead_action_pipeline");
    }
    openSalesAnalysisView() {
        this.action.doAction("sale.action_order_report_all");
    }
    openQuotationsView() {
        this.action.doAction("sale.action_quotations");
    }
    openSalesOrdersView() {
        this.action.doAction("sale.action_orders");
    }
    openProductsView() {
        this.action.doAction("sale.product_template_action");
    }
    openCustomersView() {
        this.action.doAction("account.res_partner_action_customer");
    }
    openPointOfSaleView() {
        this.action.doAction("point_of_sale.action_pos_config_kanban");
    }
    openPointOfSaleOrdersView() {
        this.action.doAction("point_of_sale.action_pos_pos_form");
    }
    openPointOfSaleProductsView() {
        this.action.doAction("point_of_sale.product_template_action_pos_product");
    }
    openPointOfSaleSalesDetailsReportView() {
        this.action.doAction("point_of_sale.action_report_pos_order_all");
    }


    openRequestsForQuotationView() {
        this.action.doAction("purchase.purchase_rfq");
    }
    openPurchaseOrdersView() {
        this.action.doAction("purchase.purchase_form_action");
    }
    openPurchaseVendorsView() {
        this.action.doAction("account.res_partner_action_supplier");
    }
    openPurchaseProductsView() {
        this.action.doAction("purchase.product_normal_action_puchased");
    }
    openPurchaseAnalysisView() {
        this.action.doAction("purchase.action_purchase_order_report_all");
    }
    



    openInventoryOverviewView() {
        this.action.doAction("stock.stock_picking_type_action");
    }
    openStockTransfersView() {
        this.action.doAction("stock.action_picking_tree_all");
    }
    openStockProductsView() {
        this.action.doAction("stock.product_template_action_product");
    }
    openStockReportView() {
        this.action.doAction("stock.action_product_stock_view");
    }
    openStockLocationsReportView() {
        this.action.doAction("stock.dashboard_open_quants");
    }
    openStockMovesHistoryReportView() {
        this.action.doAction("stock.stock_move_line_action");
    }
    openStockMovesReportView() {
        this.action.doAction("stock.stock_move_action");
    }
    openStockValuationReportView() {
        this.action.doAction("stock_account.stock_valuation_layer_action");
    }



    openOrders(title, domain) {
        this.action.doAction({
            type: "ir.actions.act_window",
            name: title,
            res_model: "ignite_dashboard.order",
            domain: new Domain(domain).toList(),
            views: [
                [false, "list"],
                [false, "form"],
            ],
        });
    }
    openLast7DaysOrders() {
        const domain =
            "[('create_date','>=', (context_today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d'))]";
        this.openOrders("Last 7 days orders", domain);
    }
    openLast7DaysCancelledOrders() {
        const domain =
            "[('create_date','>=', (context_today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')), ('state','=', 'cancelled')]";
        this.openOrders("Last 7 days cancelled orders", domain);
    }
}

IgniteDashboard.components = { Layout, Notebook, Card, PieChart, LineChart, DoughnutChart, BarChart };
IgniteDashboard.template = "ignite_dashboard.clientaction";

registry.category("actions").add("ignite_dashboard.dashboard", IgniteDashboard);
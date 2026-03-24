/** @odoo-module */

import { registry } from "@web/core/registry";
import { memoize } from "@web/core/utils/functions";

export const igniteService = {
    dependencies: ["rpc"],
    async: ["loadSaleStatistics", "loadPurchaseStatistics", "loadInventoryStatistics"],
    start(env, { rpc }) {
        return {
            loadSaleStatistics: memoize(() => rpc("/ignite_dashboard/sale/statistics")),
            loadPurchaseStatistics: memoize(() => rpc("/ignite_dashboard/purchase/statistics")),
            loadInventoryStatistics: memoize(() => rpc("/ignite_dashboard/inventory/statistics")),
        };
    },
};

registry.category("services").add("igniteService", igniteService);
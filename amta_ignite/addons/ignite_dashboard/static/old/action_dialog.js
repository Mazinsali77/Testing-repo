/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { DebugMenu } from "@web/core/debug/debug_menu";
import { ActionDialog } from "@web/webclient/actions/action_dialog";
import { useLegacyRefs } from "@web/legacy/utils";
import { BookmarkMenu } from "./bookmark_menu";

import { useEffect } from "@odoo/owl";

ActionDialog.components = { ...ActionDialog.components, BookmarkMenu };
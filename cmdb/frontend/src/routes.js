import VueRouter from 'vue-router';

let routes = [
    {
        path: '/inventory',
        component: require('./assets/inventory/Inventory.vue')
    },
    {
        path: '/inventory/:logicalName',
        component: require('./assets/inventory/InventoryDetail.vue')
    },
    {
        path: '/changemanagement',
        component: require('./assets/change_management/ChangeManagement.vue')
    },
    {
        path: '/changemanagement/:changeNumber',
        component: require('./assets/change_management/ChangeManagementDetail.vue')
    }
];

export default new VueRouter({
   routes
});
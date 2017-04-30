import VueRouter from 'vue-router';

let routes = [
    {
        path: '/inventory',
        component: require('./assets/inventory/Inventory.vue')
    },
    {
        path: '/changemanagement',
        component: require('./assets/change_management/ChangeManagement.vue')
    }
];

export default new VueRouter({
   routes
});
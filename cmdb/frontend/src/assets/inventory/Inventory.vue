<template>
    <div>
        <h1>This is My Inventory</h1>
        <filter-bar></filter-bar>
        <vuetable
                ref="vuetable"
                :api-url="url"
                :fields="fields"
                :pagination-path="paginationPath"
                @vuetable:pagination-data="onPaginationData"
                :append-params="queryParams"
        ></vuetable>
        <div class="vuetable-pagination ui basic segment grid">
            <vuetable-pagination-info ref="paginationInfo"
            ></vuetable-pagination-info>

            <vuetable-pagination ref="pagination"
                                 @vuetable-pagination:change-page="onChangePage"
            ></vuetable-pagination>
        </div>
    </div>
</template>

<script>
import Vuetable from 'vuetable-2/src/components/Vuetable.vue'
import VuetablePagination from 'vuetable-2/src/components/VuetablePagination.vue'
import VuetablePaginationInfo from 'vuetable-2/src/components/VuetablePaginationInfo.vue'
import FilterBar from './FilterBar.vue'
import {Mixin} from 'semantic-ui-vue2'

export default {
    name: 'inventory',
    mixins: [Mixin],
    components: {
        Vuetable,
        VuetablePagination,
        VuetablePaginationInfo,
        FilterBar,
    },
    data() {
        return {
            url: "http://vuetable.ratiw.net/api/users",
            paginationPath: '',
            queryParams: {},
            fields: [
                {
                    title: 'Full Name',
                    name: 'name',
                    titleClass: 'text-left',
                    dataClass: 'text-left',
                    callback: 'fullname',
                    sortField: 'name',
                },
                {
                    title: 'Email Address',
                    name: 'email',
                    titleClass: 'text-left',
                    dataClass: 'text-left',
                },
                {
                    title: 'Date of Birth',
                    name: 'birthdate',
                    titleClass: 'text-center',
                    dataClass: 'text-center',
                },
            ],
        }
    },
    mounted() {
        this.$events.fire('module:mounted', 'inventory')
        this.$events.$on('inventory:filter:set', data => {
            this.queryParams = {
                'filter': data,
            };
            Vue.nextTick(() => this.$refs.vuetable.refresh())
        });
        this.$events.$on('inventory:filter:reset', () => {
            this.queryParams = {};
            Vue.nextTick(() => this.$refs.vuetable.refresh())
        })
    },
    methods: {
        fullname(value) {
            return value.toUpperCase()
        },
        onPaginationData (paginationData) {
            this.$refs.pagination.setPaginationData(paginationData);
            this.$refs.paginationInfo.setPaginationData(paginationData)
        },
        onChangePage (page) {
            this.$refs.vuetable.changePage(page)
        },
    },
}
</script>
<template>
    <div>
        <h1>This is My Inventory</h1>
        <vuetable
                ref="vuetable"
                :api-url="url"
                :fields="fields"
                :pagination-path="paginationPath"
                @vuetable:pagination-data="onPaginationData"
        ></vuetable>
        <vuetable-pagination
                ref="pagination"
                @vuetable-pagination:change-page="onChangePage"
        ></vuetable-pagination>
    </div>
</template>

<script>
import Vuetable from 'vuetable-2/src/components/Vuetable.vue'
import VuetablePagination from 'vuetable-2/src/components/VuetablePagination.vue'
import {Mixin} from 'semantic-ui-vue2'

export default {
    name: 'inventory',
    mixins: [Mixin],
    components: { Vuetable, VuetablePagination },
    data() {
        return {
            url: "http://vuetable.ratiw.net/api/users",
            paginationPath: '',
            fields: [
                {
                    title: 'Full Name',
                    name: 'name',
                    titleClass: 'text-left',
                    dataClass: 'text-left',
                    callback: 'fullname',
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
        Event.$emit('inventoryMounted')
    },
    methods: {
        fullname(value) {
            return value.toUpperCase()
        },
        onPaginationData (paginationData) {
            this.$refs.pagination.setPaginationData(paginationData)
        },
        onChangePage (page) {
            this.$refs.vuetable.changePage(page)
        },
    },
}
</script>
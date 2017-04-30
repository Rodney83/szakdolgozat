<template>
    <h1>This is The Change Management</h1>
</template>

<script>
export default {
    name: 'changeManagement',
    data() {
        return {
            title: 'changeManagement',
            subTitle: '',
        }
    },

    mounted() {
        Event.$emit('changeManagementMounted')
    },
}
</script>
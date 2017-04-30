<template>
    <h1>This is My Inventory</h1>
</template>

<script>
export default {
    name: 'inventory',
    data() {
        return {
            title: 'Inventory',
            subTitle: '',
        }
    },
    mounted() {
        Event.$emit('inventoryMounted')
    },
}
</script>
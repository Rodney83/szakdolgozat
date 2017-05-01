<template>
    <div>
        <h1>{{title}}</h1>
        <h2>{{ln}}</h2>
    </div>
</template>

<script>
export default {
    name: 'inventoryDetail',
    data() {
        return {
            title: 'Inventory Detail',
            ln: this.$route.params.logicalName,
        }
    },
}
</script>
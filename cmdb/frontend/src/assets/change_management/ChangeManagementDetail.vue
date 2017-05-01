<template>
    <div>
        <h1>{{title}}</h1>
        <h2>{{cn}}</h2>
    </div>
</template>

<script>
export default {
    name: 'changeManagementDetail',
    data() {
        return {
            title: 'ChangeManagement Detail',
            cn: this.$route.params.changeNumber,
        }
    },
}
</script>
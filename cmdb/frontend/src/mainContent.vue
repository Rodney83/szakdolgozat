<template>
    <div>
        <!-- Content Header (Page header) -->
        <section class="content-header">
          <h1>
            {{componentTitle}}
            <small>{{componentSubTitle}}</small>
          </h1>
        </section>

        <!-- Main content -->
        <section class="content">
          <!-- Your Page Content Here -->
          <router-view></router-view>
        </section>
        <!-- /.content -->
    </div>
</template>

<script>
export default {
    name: 'mainContent',
    props: ['activeModule'],
    data() {
        return {
            componentTitle: this.activeModule,
            componentSubTitle: '',
        }
    },
}
</script>
<template>
  <div class="wrapper">
  <!-- Main Header -->
  <header class="main-header">

    <!-- Logo -->
    <a href="#" class="logo">
      <!-- mini logo for sidebar mini 50x50 pixels -->
      <span class="logo-mini">CMDB<</span>
      <!-- logo for regular state and mobile devices -->
      <span class="logo-lg"><b>CMDB</b></span>
    </a>

    <!-- Header Navbar -->
    <nav class="navbar navbar-static-top" role="navigation">
      <!-- Sidebar toggle button-->
      <a href="#" class="sidebar-toggle" data-toggle="offcanvas" role="button">
        <span class="sr-only">Toggle navigation</span>
      </a>
      <!-- Navbar Right Menu -->
      <div class="navbar-custom-menu">
        <ul class="nav navbar-nav">
          <!-- User Account Menu -->
          <li class="dropdown user user-menu">
            <!-- Menu Toggle Button -->
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">
              <span class="hidden-xs">{{user.name}}</span>
            </a>
            <ul class="dropdown-menu">
              <!-- The user image in the menu -->
              <li class="user-header">
                <p>
                  {{user.name}}
                </p>
              </li>
              <!-- Menu Body -->
              <li class="user-body">
                <div class="row">
                  <div class="col-xs-4 text-center">
                    <a href="#">Followers</a>
                  </div>
                  <div class="col-xs-4 text-center">
                    <a href="#">Sales</a>
                  </div>
                  <div class="col-xs-4 text-center">
                    <a href="#">Friends</a>
                  </div>
                </div>
                <!-- /.row -->
              </li>
              <!-- Menu Footer-->
              <li class="user-footer">
                <div class="pull-left">
                  <a href="#" class="btn btn-default btn-flat">Profile</a>
                </div>
                <div class="pull-right">
                  <a href="#" class="btn btn-default btn-flat">Sign out</a>
                </div>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
  </header>
  <!-- Left side column. contains the logo and sidebar -->
  <aside class="main-sidebar">

    <!-- sidebar: style can be found in sidebar.less -->
    <section class="sidebar">

      <!-- Sidebar user panel (optional) -->
      <div class="user-panel">
        <div class="pull-left image">
          <img src="./assets/logo.png" class="img-circle" alt="User Image">
        </div>
        <div class="pull-left info">
          <p>{{user.name}}</p>
        </div>
      </div>

      <!-- Sidebar Menu -->
      <ul class="sidebar-menu">
        <!-- Optionally, you can add icons to the links -->
        <li v-bind:class="{ active: inventory}">
          <router-link to="/inventory">
            <i class="fa fa-link"></i> <span>Inventory</span>
          </router-link>
        </li>
        <li v-bind:class="{ active: changeManagement}">
          <router-link to="/changemanagement" v-bind:class="{ active: changeManagement}">
            <i class="fa fa-link"></i><span>Change Management</span>
          </router-link>
        </li>
      </ul>
      <!-- /.sidebar-menu -->
    </section>
    <!-- /.sidebar -->
  </aside>

  <!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper">
      <main-content v-bind:title="moduleTitle"></main-content>
  </div>
  <!-- /.content-wrapper -->

  <!-- Main Footer -->
  <footer class="main-footer">
    <!-- To the right -->
    <div class="pull-right hidden-xs">
      Anything you want
    </div>
    <!-- Default to the left -->
    <strong>Copyright &copy; 2016 <a href="#">Company</a>.</strong> All rights reserved.
  </footer>
</div>
</template>

<script>
import mainContent from './mainContent.vue'

export default {
    name: 'app',
    components: {mainContent},
    data () {
        return {
            moduleTitle: '',
            inventory: false,
            changeManagement: false,
            user: {
                name: 'Tamas Pasztor'
            },
        }
    },
    created() {
        this.$events.$on('module:mounted', (data) => {
            if (data === 'inventory') {
                this.inventory = true;
                this.changeManagement = false;
                this.moduleTitle = 'Inventory';
            } else if (data === 'changes') {
                this.inventory = false;
                this.changeManagement = true;
                this.moduleTitle = 'Change Management';
            }
        });
    }
}
</script>


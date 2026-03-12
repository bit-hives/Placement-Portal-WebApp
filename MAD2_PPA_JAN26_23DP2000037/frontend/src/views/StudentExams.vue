<template>
  <div class="d-flex min-vh-100 bg-light font-sans">
    
    <div class="bg-white shadow-sm d-flex flex-column" style="width: 250px;">
      <div class="p-4 border-bottom text-center">
        <h4 class="fw-bold text-primary mb-0">PlacementPortal</h4>
        <span class="badge bg-primary mt-2">Student Portal</span>
      </div>
      <div class="p-3 flex-grow-1">
        <ul class="nav flex-column gap-2">
          <li class="nav-item">
            <router-link to="/student/dashboard" class="nav-link rounded-3 text-dark fw-semibold"><i class="bi bi-grid-fill me-2"></i> Dashboard</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/student/profile" class="nav-link rounded-3 text-dark fw-semibold"><i class="bi bi-person-badge-fill me-2"></i> My Profile</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/student/notifications" class="nav-link rounded-3 text-dark fw-semibold"><i class="bi bi-bell-fill me-2"></i> Alerts & Off-Campus</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/student/exams" class="nav-link rounded-3 text-white fw-semibold bg-primary"><i class="bi bi-pencil-square me-2"></i> Online Exams</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/student/placement" class="nav-link rounded-3 text-dark fw-semibold"><i class="bi bi-award-fill me-2"></i> Application Status</router-link>
          </li>
        </ul>
      </div>
      <div class="p-4 border-top">
        <button @click="$store.commit('LOGOUT'); $router.push('/login')" class="btn btn-light w-100 text-start fw-semibold text-danger"><i class="bi bi-box-arrow-right me-2"></i> Logout</button>
      </div>
    </div>

    
    <div class="flex-grow-1 d-flex flex-column">
      
      <nav class="navbar navbar-light bg-white shadow-sm px-4 py-3">
        <h5 class="mb-0 fw-bold text-dark">Pre-Placement Exams</h5>
        <div class="ms-auto d-flex align-items-center gap-3">
          <button class="btn btn-light rounded-circle p-2 position-relative"><i class="bi bi-bell-fill"></i></button>
          <div class="d-flex align-items-center gap-2 bg-light px-3 py-1 rounded-pill border ms-2">
            <div class="bg-primary text-white rounded-circle d-flex justify-content-center align-items-center fw-bold" style="width: 32px; height: 32px;">
              <i class="bi bi-person-fill"></i>
            </div>
            <span class="fw-semibold small">{{ $store.state.username }}</span>
          </div>
        </div>
      </nav>

      
      <div class="p-4 flex-grow-1 d-flex justify-content-center align-items-center">
        <div class="text-center">
          <h3 class="fw-bold text-dark">Exam Module Offline</h3>
          <p class="text-muted fs-5 mx-auto" style="max-width: 500px;">
            The central placement examination coordination module will be enabled in Phase 3 of deployment. 
            Currently, companies process exams via standalone third-party systems.
          </p>
          <router-link to="/student/dashboard" class="btn btn-primary rounded-pill px-5 fw-bold mt-3 shadow-sm">Return to Dashboard</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default { }
</script>

<style scoped>
.font-sans { font-family: 'Inter', system-ui, -apple-system, sans-serif; }
.nav-link:not(.bg-primary):hover { background-color: #f8f9fa; }
</style>

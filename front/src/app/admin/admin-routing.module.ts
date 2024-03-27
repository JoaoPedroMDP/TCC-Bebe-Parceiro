import { Routes } from '@angular/router';
import { HomeComponent } from './index';
import { AuthGuard } from '../auth/guards/auth.guard';

export const AdminRouting: Routes = [
//   { path: 'admin', component: HomeComponent},
  {
    path: 'admin',
    component: HomeComponent, 
    children: [
    //   { path: '', component: DashboardFinanceiroComponent, canActivate: [FinanceiroGuard] },,
    ],
    canActivate: [AuthGuard], 
    data: { expectedRole: 'admin' }
  },
];
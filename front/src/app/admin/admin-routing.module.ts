import { Routes } from '@angular/router';
import { HomeComponent } from './index';

export const AdminRouting: Routes = [
//   { path: 'admin', component: HomeComponent},
  {
    path: 'admin',
    component: HomeComponent, children: [
    //   { path: '', component: DashboardFinanceiroComponent, canActivate: [FinanceiroGuard] },,
    ],
    // canActivate: [FinanceiroGuard]
  },
];
import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';

export const BenefitedRouting: Routes = [
//   { path: 'admin', component: HomeComponent},
{
    path: 'beneficiada',
    component: HomeComponent, children: [
    //   { path: '', component: DashboardFinanceiroComponent, canActivate: [FinanceiroGuard] },,
    ],
    // canActivate: [FinanceiroGuard]
  },
];


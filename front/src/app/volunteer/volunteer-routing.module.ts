import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';

export const VolunteerRouting: Routes = [
//   { path: 'voluntaria', component: HomeComponent},
{
    path: 'voluntaria',
    component: HomeComponent, children: [
    //   { path: '', component: DashboardFinanceiroComponent, canActivate: [FinanceiroGuard] },,
    ],
    // canActivate: [FinanceiroGuard]
  },
];


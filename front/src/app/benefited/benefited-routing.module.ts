import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { AuthGuard } from '../auth/guards/auth.guard';
import { MainComponent } from './index';

export const BenefitedRouting: Routes = [
  //   { path: 'admin', component: HomeComponent},
  {
    path: 'beneficiada',
    component: MainComponent,
    children: [
      { path: '', component: HomeComponent, canActivate: [AuthGuard] },
      // { path: '', component: HomeComponent, canActivate: [FinanceiroGuard] },
    ],
    canActivate: [AuthGuard],
    data: { expectedRole: 'beneficiary' }
  },
];

import { Routes } from '@angular/router';
import { ProfessionalComponent } from './components/professional.component';
import { AuthGuard } from '../auth/guards/auth.guard';

export const BenefitedRouting: Routes = [
//   { path: 'admin', component: HomeComponent},
{
    path: 'beneficiada',
    component: ProfessionalComponent, 
    children: [
    //   { path: '', component: DashboardFinanceiroComponent, canActivate: [FinanceiroGuard] },,
    ],
    canActivate: [AuthGuard], 
    data: { expectedRole: 'beneficiary' }
  },
];

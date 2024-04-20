import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { AuthGuard } from '../auth/guards/auth.guard';
import { MainComponent, ViewInformationComponent } from './index';

export const BeneficiaryRouting: Routes = [
  {
    path: 'beneficiada',
    component: MainComponent,
    children: [
      { path: '', component: HomeComponent, canActivate: [AuthGuard], data: { expectedRole: 'beneficiary' }  },
      { path: 'meus-dados', component: ViewInformationComponent, canActivate: [AuthGuard], data: { expectedRole: 'beneficiary' }  },
    ],
    canActivate: [AuthGuard],
    data: { expectedRole: 'beneficiary' }
  },
];

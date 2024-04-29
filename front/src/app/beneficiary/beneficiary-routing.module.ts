import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { AuthGuard } from '../auth/guards/auth.guard';
import { EditInformationComponent, MainComponent, ViewInformationComponent } from './index';

export const BeneficiaryRouting: Routes = [
  {
    path: 'beneficiada',
    component: MainComponent,
    children: [
      { path: '', component: HomeComponent },
      { path: 'meus-dados', component: ViewInformationComponent },
      { path: 'alterar-dados', component: EditInformationComponent },
      // { path: 'dasuhduahduas', component: EditInformationComponent, canActivate: [AuthGuard], data: { expectedRole: ['beneficiary'] } },
      // As próximas rotas só podem ser acessadas por 'beneficiary'
    ],
    canActivate: [AuthGuard],
    data: { expectedRole: ['beneficiary', 'pending_beneficiary'] }
  },
];

import { Routes } from '@angular/router';
import { AuthGuard } from '../auth/guards/auth.guard';
import { ListAppointmentComponent } from './components/appointment';
import { InspectCampaignComponent, ListCampaignComponent } from './components/campaign';
import { HomeComponent } from './components/home/home.component';
import { EditInformationComponent, MainComponent, ViewInformationComponent } from './index';

export const BeneficiaryRouting: Routes = [
  {
    path: 'beneficiada',
    component: MainComponent,
    children: [
      { path: '', component: HomeComponent },
      { path: 'meus-dados', component: ViewInformationComponent },
      { path: 'alterar-dados', component: EditInformationComponent },
      // As próximas rotas só podem ser acessadas por data: { expectedRole: ['beneficiary']
      {
        path: 'campanhas', canActivate: [AuthGuard], data: { expectedRole: ['beneficiary'] },
        children: [
          { path: '', component: ListCampaignComponent },
          { path: 'inspecionar/:idCampanha', component: InspectCampaignComponent },
        ]
      },
      {
        path: 'atendimentos', canActivate: [AuthGuard], component: ListAppointmentComponent, data: { expectedRole: ['beneficiary'] }
      },
    ],
    canActivate: [AuthGuard],
    data: { expectedRole: ['beneficiary', 'pending_beneficiary'] }
  },
];

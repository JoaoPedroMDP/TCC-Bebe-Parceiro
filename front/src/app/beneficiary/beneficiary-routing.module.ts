import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { AuthGuard } from '../auth/guards/auth.guard';
import { EditInformationComponent, MainComponent, ViewInformationComponent } from './index';
import { InspectCampaignComponent, ListCampaignComponent } from './components/campaign';
import { InspectAppointmentComponent, ListAppointmentComponent } from './components/appointment';

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
        path: 'atendimentos', canActivate: [AuthGuard], data: { expectedRole: ['beneficiary', 'pending_beneficiary'] },
        children: [
          { path: '', component: ListAppointmentComponent },
          { path: 'inspecionar/:idAtendimento', component: InspectAppointmentComponent },
        ]
      },
     
    
    ],
    canActivate: [AuthGuard],
    data: { expectedRole: ['beneficiary', 'pending_beneficiary'] }
  },
];

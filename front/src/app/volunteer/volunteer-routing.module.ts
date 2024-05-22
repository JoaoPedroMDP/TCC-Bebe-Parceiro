import { Routes } from '@angular/router';
import { AuthGuard } from '../auth/guards/auth.guard';
import { VolunteerPermisionsGuard } from '../auth/guards/volunteer-permisions.guard';
import { CreateBeneficiaryComponent, EditBeneficiaryComponent, InspectBeneficiaryComponent, ListBeneficiaryComponent } from './components/beneficiary';
import { ListCampaignComponent } from './components/campaign';
import { ListGroupsComponent } from './components/groups';
import { ListPendingProfessionalsComponent, ListProfessionalComponent } from './components/professional';
import { ListSpecialitiesComponent } from './components/specialities';
import { ListSwapComponent } from './components/swap';
import { ListVolunteerComponent } from './components/volunteer';
import { HomeComponent, MainComponent } from './index';


export const VolunteerRouting: Routes = [
  {
    path: 'voluntaria',
    component: MainComponent,
    canActivate: [AuthGuard],
    data: { expectedRole: 'volunteer' },
    children: [
      { path: '', component: HomeComponent },
      {
        path: 'beneficiadas',
        canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['Beneficiárias'] },
        children: [
          { path: '', component: ListBeneficiaryComponent },
          { path: 'criar', component: CreateBeneficiaryComponent },
          { path: 'inspecionar/:idBeneficiada', component: InspectBeneficiaryComponent },
          { path: 'editar/:idBeneficiada', component: EditBeneficiaryComponent }
        ]
      },
      {
        path: 'profissionais',
        canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['Profissionais'] },
        children: [
          { path: '', component: ListProfessionalComponent },
          { path: 'pendentes', component: ListPendingProfessionalsComponent },
        ]
      },
      {
        path: 'voluntarias', component: ListVolunteerComponent, canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['Voluntárias'] }
      },
      {
        path: 'especialidades', component: ListSpecialitiesComponent, canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['Especialidades'] },
      },
      {
        path: 'campanhas', component: ListCampaignComponent, canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['Campanhas'] },
      },
      {
        path: 'funcoes', component: ListGroupsComponent, canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['Voluntárias'] },
      },
      {
        path: 'trocas', component: ListSwapComponent, canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['Trocas'] }
      }
    ]
  },
];


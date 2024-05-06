import { Routes } from '@angular/router';
import { AuthGuard } from '../auth/guards/auth.guard';
import { CreateBeneficiaryComponent, EditBeneficiaryComponent, InspectBeneficiaryComponent, ListBeneficiaryComponent } from './components/beneficiary';
import { CreateEditVolunteerComponent,InspectVolunteerComponent, ListVolunteerComponent } from './components/volunteer';
import { ListPendingProfessionalsComponent, ListProfessionalComponent } from './components/professional';
import { ListSpecialitiesComponent } from './components/specialities';
import { HomeComponent, MainComponent } from './index';
import { VolunteerPermisionsGuard } from '../auth/guards/volunteer-permisions.guard';
import { ListCampaignComponent } from './components/campaign/list-campaign/list-campaign.component';


export const VolunteerRouting: Routes = [
  {
    path: 'voluntaria',
    component: MainComponent,
    canActivate: [AuthGuard],
    data: { expectedRole: 'volunteer' },
    children: [
      { path: '', component: HomeComponent },
      {
        path: 'beneficiadas',      // BENEFICIADAS
        canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['manage_beneficiaries'] },
        children: [
          { path: '', component: ListBeneficiaryComponent },
          { path: 'criar', component: CreateBeneficiaryComponent },
          { path: 'inspecionar/:idBeneficiada', component: InspectBeneficiaryComponent },
          { path: 'editar/:idBeneficiada', component: EditBeneficiaryComponent }
        ]
      },
      {
        path: 'voluntarias',      // VOLUNTARIAS
        canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['manage_volunteers'] },
        children: [
          { path: '', component: ListVolunteerComponent },
          { path: 'criar', component: CreateEditVolunteerComponent },
          { path: 'inspecionar/:idVoluntaria', component: InspectVolunteerComponent },
        ]
      },
      {
        path: 'profissionais',      // PROFISSIONAL
        canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['manage_professionals'] },
        children: [
          { path: '', component: ListProfessionalComponent },
          { path: 'pendentes', component: ListPendingProfessionalsComponent },
        ]
      },
      {
        path: 'especialidades', component: ListSpecialitiesComponent, canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['manage_specialities'] },
      },

      {
        path: 'campanhas',      
        canActivate: [VolunteerPermisionsGuard],
        data: { requiredPermissions: ['manage_volunteers'] },
        children: [
          { path: '', component: ListCampaignComponent },
          
        ]
      },

   
    ]
  },
];



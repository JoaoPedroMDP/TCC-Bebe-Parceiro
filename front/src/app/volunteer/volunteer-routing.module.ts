import { Routes } from '@angular/router';
import { AuthGuard } from '../auth/guards/auth.guard';
import { CreateBeneficiaryComponent, EditBeneficiaryComponent, InspectBeneficiaryComponent, ListBeneficiaryComponent } from './components/beneficiary';
import { HomeComponent } from './components/home/home.component';
import { MainComponent } from './index';


export const VolunteerRouting: Routes = [
  {
    path: 'voluntaria',
    component: MainComponent,
    children: [
      { path: '', component: HomeComponent, canActivate: [AuthGuard], data: { expectedRole: 'volunteer' } },
      // BENEFICIADAS
      { path: 'beneficiadas', component: ListBeneficiaryComponent, canActivate: [AuthGuard], data: { expectedRole: 'volunteer' } },
      { path: 'beneficiadas/criar', component: CreateBeneficiaryComponent, canActivate: [AuthGuard], data: { expectedRole: 'volunteer' } },
      { path: 'beneficiadas/inspecionar/:idBeneficiada', component: InspectBeneficiaryComponent, canActivate: [AuthGuard], data: { expectedRole: 'volunteer' } },
      { path: 'beneficiadas/editar/:idBeneficiada', component: EditBeneficiaryComponent, canActivate: [AuthGuard], data: { expectedRole: 'volunteer' } },
    ],
    canActivate: [AuthGuard],
    data: { expectedRole: 'volunteer' }
  },


];

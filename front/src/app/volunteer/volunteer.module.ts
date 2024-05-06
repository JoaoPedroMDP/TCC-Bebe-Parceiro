import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AuthModule } from '../auth/auth.module';
import { CreateBeneficiaryComponent, DeleteBeneficiaryComponent, EditBeneficiaryComponent, InspectBeneficiaryComponent, ListBeneficiaryComponent } from './components/beneficiary';
import { CreateEditVolunteerComponent, DeleteVolunteerComponent, InspectVolunteerComponent, ListVolunteerComponent } from './components/volunteer';
import { ApproveRefuseProfessionalComponent, CreateEditProfessionalComponent, DeleteProfessionalComponent, InspectProfessionalComponent, ListPendingProfessionalsComponent, ListProfessionalComponent } from './components/professional';
import { CreateEditSpecialityComponent, DeleteSpecialityComponent, ListSpecialitiesComponent } from './components/specialities';
import { AcessCodesModalComponent, HomeComponent, MainComponent, VolunteerService } from './index';
import { CreateEditCampaignComponent } from './components/campaign/create-edit-campaign/create-edit-campaign.component';
import { ListCampaignComponent } from './components/campaign/list-campaign/list-campaign.component';
import { DeleteCampaignComponent } from './components/campaign/delete-campaign/delete-campaign.component';
import { InspectCampaignComponent } from './components/campaign/inspect-campaign/inspect-campaign.component';






@NgModule({
  declarations: [
    // MAIN
    HomeComponent,
    MainComponent,
    AcessCodesModalComponent,
    // BENEFICIARY
    ListBeneficiaryComponent,
    InspectBeneficiaryComponent,
    CreateBeneficiaryComponent,
    EditBeneficiaryComponent,
    DeleteBeneficiaryComponent,
    // VOLUNTEERS
    ListVolunteerComponent,
    InspectVolunteerComponent,
    CreateEditVolunteerComponent,
    DeleteVolunteerComponent,
   
    // PROFESSIONAL
    ListProfessionalComponent,
    InspectProfessionalComponent,
    DeleteProfessionalComponent,
    ListPendingProfessionalsComponent,
    ApproveRefuseProfessionalComponent,
    CreateEditProfessionalComponent,
    // ESPECIALIDADES
    ListSpecialitiesComponent,
    CreateEditSpecialityComponent,
    DeleteSpecialityComponent,
    CreateEditCampaignComponent,
    //CAMPANHAS
    ListCampaignComponent,
    DeleteCampaignComponent,
    InspectCampaignComponent,
    // FUNÇÕES
    
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    AuthModule,
    NgxMaskModule.forRoot()
  ],
  providers: [
    VolunteerService
  ]
})
export class VolunteerModule { }





import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AuthModule } from '../auth/auth.module';
import { CreateBeneficiaryComponent, DeleteBeneficiaryComponent, EditBeneficiaryComponent, InspectBeneficiaryComponent, ListBeneficiaryComponent } from './components/beneficiary';
import { CreateEditCampaignComponent, DeleteCampaignComponent, InspectCampaignComponent, ListCampaignComponent } from './components/campaign';
import { InspectGroupsComponent, ListGroupsComponent } from './components/groups';
import { ApproveRefuseProfessionalComponent, CreateEditProfessionalComponent, DeleteProfessionalComponent, InspectProfessionalComponent, ListPendingProfessionalsComponent, ListProfessionalComponent } from './components/professional';
import { CreateEditSpecialityComponent, DeleteSpecialityComponent, ListSpecialitiesComponent } from './components/specialities';
import { ApproveRefuseSwapComponent, CreateSwapComponent, DeleteSwapComponent, EditSwapComponent, InspectSwapComponent, ListSwapComponent } from './components/swap';
import { CreateVolunteerComponent, DeleteVolunteerComponent, EditVolunteerComponent, InspectVolunteerComponent, ListVolunteerComponent } from './components/volunteer';
import { AcessCodesModalComponent, HomeComponent, MainComponent, VolunteerService } from './index';

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
    CreateVolunteerComponent,
    EditVolunteerComponent,
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
    //CAMPANHAS
    CreateEditCampaignComponent,
    ListCampaignComponent,
    DeleteCampaignComponent,
    InspectCampaignComponent,
    // FUNÇÕES
    ListGroupsComponent,
    InspectGroupsComponent,
    // TROCAS
    DeleteSwapComponent, 
    InspectSwapComponent, 
    ListSwapComponent, 
    ApproveRefuseSwapComponent, 
    CreateSwapComponent, 
    EditSwapComponent
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





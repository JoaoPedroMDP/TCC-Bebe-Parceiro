import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AuthModule } from '../auth/auth.module';
import { ApproveAppointmentComponent, CreateAppointmentComponent, DeleteAppointmentComponent, EditAppointmentComponent, InspectAppointmentComponent, ListAppointmentComponent, ListPendingAppointmentsComponent } from './components/appointment';
import { CreateBeneficiaryComponent, DeleteBeneficiaryComponent, EditBeneficiaryComponent, InspectBeneficiaryComponent, ListBeneficiaryComponent } from './components/beneficiary';
import { CreateEditCampaignComponent, DeleteCampaignComponent, InspectCampaignComponent, ListCampaignComponent } from './components/campaign';
import { ApproveBeneficiaryComponent, AssignedEvaluationsComponent, InspectEvaluationComponent, PendingEvaluationsComponent } from './components/evaluations';
import { InspectGroupsComponent, ListGroupsComponent } from './components/groups';
import { ApproveRefuseProfessionalComponent, CreateEditProfessionalComponent, DeleteProfessionalComponent, InspectProfessionalComponent, ListPendingProfessionalsComponent, ListProfessionalComponent } from './components/professional';
import { DateRangeReportsModalComponent, ListReportsComponent } from './components/reports';
import { CreateEditSpecialityComponent, DeleteSpecialityComponent, ListSpecialitiesComponent } from './components/specialities';
import { CreateSwapComponent, DeleteSwapComponent, EditSwapComponent, InspectSwapComponent, ListSwapComponent } from './components/swap';
import { CreateVolunteerComponent, DeleteVolunteerComponent, EditVolunteerComponent, InspectVolunteerComponent, ListVolunteerComponent } from './components/volunteer';
import { AcessCodesModalComponent, HomeComponent, MainComponent, VolunteerService } from './index';
import { ListBeneficiaryRecordsComponent } from './components/evaluations/list-beneficiary-records/list-beneficiary-records.component';

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
    CreateSwapComponent, 
    EditSwapComponent, 
    // RELATORIOS
    ListReportsComponent, 
    DateRangeReportsModalComponent, 
    // ATENDIMENTOS
    ListAppointmentComponent, 
    InspectAppointmentComponent, 
    ListPendingAppointmentsComponent, 
    ApproveAppointmentComponent,
    DeleteAppointmentComponent, 
    CreateAppointmentComponent, 
    EditAppointmentComponent,
    // ADMISSÕES
    PendingEvaluationsComponent, 
    ApproveBeneficiaryComponent, 
    AssignedEvaluationsComponent, 
    InspectEvaluationComponent, ListBeneficiaryRecordsComponent
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





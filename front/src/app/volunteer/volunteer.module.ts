import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AuthModule } from '../auth/auth.module';
import { CreateBeneficiaryComponent, DeleteBeneficiaryComponent, EditBeneficiaryComponent, InspectBeneficiaryComponent, ListBeneficiaryComponent } from './components/beneficiary';
import { ApproveRefuseProfessionalComponent, CreateEditProfessionalComponent, DeleteProfessionalComponent, InspectProfessionalComponent, ListPendingProfessionalsComponent, ListProfessionalComponent } from './components/professional';
import { CreateEditSpecialityComponent, DeleteSpecialityComponent, ListSpecialitiesComponent } from './components/specialities';
import { AcessCodesModalComponent, HomeComponent, MainComponent, VolunteerService } from './index';
import { ListSwapComponent } from './components/swap/list-swap/list-swap.component';
import { InspectSwapComponent } from './components/swap/inspect-swap/inspect-swap.component';
import { DeleteSwapComponent } from './components/swap/delete-swap/delete-swap.component';
import { CreateEditSwapComponent } from './components/swap/create-edit-swap/create-edit-swap.component';



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
    // TROCAS
    ListSwapComponent,
    ListSwapComponent,
    InspectSwapComponent,
    DeleteSwapComponent,
    CreateEditSwapComponent,
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





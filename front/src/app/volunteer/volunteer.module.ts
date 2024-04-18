import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AcessCodesModalComponent, HomeComponent, MainComponent, VolunteerService } from './index';
import { ListBeneficiaryComponent, DeleteBeneficiaryComponent, CreateBeneficiaryComponent, InspectBeneficiaryComponent, EditBeneficiaryComponent } from './components/beneficiary';
import { AuthModule } from '../auth/auth.module';
import { ListProfessionalComponent } from './components/professional/list-professional/list-professional.component';



@NgModule({
  declarations: [
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





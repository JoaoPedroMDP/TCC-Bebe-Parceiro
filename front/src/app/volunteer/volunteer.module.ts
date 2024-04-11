import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AcessCodesModalComponent, HomeComponent, MainComponent, VolunteerService } from './index';
import { ListBeneficiaryComponent, DeleteBeneficiaryComponent, CreateBeneficiaryComponent, InspectBeneficiaryComponent } from './components/beneficiary';
import { AuthModule } from '../auth/auth.module';
import { EditBeneficiaryComponent } from './components/beneficiary/edit-beneficiary/edit-beneficiary.component';



@NgModule({
  declarations: [
    HomeComponent,
    AcessCodesModalComponent,
    MainComponent,
    // BENEFICIARY
    ListBeneficiaryComponent,
    InspectBeneficiaryComponent,
    CreateBeneficiaryComponent,
    EditBeneficiaryComponent,
    DeleteBeneficiaryComponent,
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





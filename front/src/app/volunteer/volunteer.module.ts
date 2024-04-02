import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AcessCodesModalComponent, HomeComponent, MainComponent, VolunteerService } from './index';
import { ListBeneficiaryComponent } from './components/beneficiary';


@NgModule({
  declarations: [
    HomeComponent,
    AcessCodesModalComponent,
    MainComponent,
    ListBeneficiaryComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    NgxMaskModule.forRoot()
  ],
  providers: [
    VolunteerService
  ]
})
export class VolunteerModule { }





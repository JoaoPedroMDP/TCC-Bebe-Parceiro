import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { BeneficiaryService, HomeComponent, MainComponent, RemoveInformationComponent, ViewInformationComponent } from './index';


@NgModule({
  declarations: [
    HomeComponent,
    MainComponent,
    ViewInformationComponent,
    RemoveInformationComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    NgxMaskModule.forRoot()
  ],
  providers: [
    BeneficiaryService
  ]
})
export class BeneficiaryModule { }





import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { BeneficiaryService, EditInformationComponent, HomeComponent, MainComponent, RemoveInformationComponent, ViewInformationComponent } from './index';
import { AuthModule } from '../auth/auth.module';


@NgModule({
  declarations: [
    HomeComponent,
    MainComponent,
    ViewInformationComponent,
    RemoveInformationComponent,
    EditInformationComponent
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
    BeneficiaryService
  ]
})
export class BeneficiaryModule { }





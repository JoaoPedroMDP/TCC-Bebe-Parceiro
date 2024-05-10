import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AuthModule } from '../auth/auth.module';
import { InspectCampaignComponent, ListCampaignComponent } from './components/campaign';
import { BeneficiaryService, EditInformationComponent, HomeComponent, MainComponent, RemoveInformationComponent, RequestSwapComponent, ViewInformationComponent } from './index';


@NgModule({
  declarations: [
    HomeComponent,
    MainComponent,
    ViewInformationComponent,
    RemoveInformationComponent,
    EditInformationComponent,
    InspectCampaignComponent,
    ListCampaignComponent,
    RequestSwapComponent
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





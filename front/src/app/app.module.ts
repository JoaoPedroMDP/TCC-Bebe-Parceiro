import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AdminModule, AppComponent, AppRoutingModule, AuthModule, BenefitedModule } from './index';
import { VolunteerModule } from './volunteer/volunteer.module';
import { CookieService } from 'ngx-cookie-service';
import { ProfessionalModule } from './professional/professional.module';


@NgModule({
  declarations: [
    AppComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    AuthModule,
    AdminModule,
    BenefitedModule,
    VolunteerModule,
    ProfessionalModule,
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }

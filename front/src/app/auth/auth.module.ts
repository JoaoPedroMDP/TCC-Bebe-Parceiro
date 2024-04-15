import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { RecaptchaModule } from 'ng-recaptcha';
import { NgxMaskModule } from 'ngx-mask';
import { AutoCadastroComponent, ChildrenComponent, CodigoAcessoComponent, ErrorComponent, LoginComponent, ProfessionalComponent, SucessoCadastroComponent, ValidCodeGuard } from './index';



@NgModule({
  declarations: [
    CodigoAcessoComponent,
    AutoCadastroComponent,
    SucessoCadastroComponent,
    ChildrenComponent,
    LoginComponent,
    ErrorComponent,
    ProfessionalComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    RecaptchaModule,
    NgxMaskModule.forRoot()
  ],
  providers: [
    ValidCodeGuard
  ],
  exports: [ChildrenComponent]
})
export class AuthModule { }





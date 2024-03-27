import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { AutoCadastroComponent, ChildrenComponent, CodigoAcessoComponent, ErrorComponent, LoginComponent, SucessoCadastroComponent, ValidCodeGuard } from './index';
import { ProfessionalComponent } from './components/components_professional/professional.component';


@NgModule({
  declarations: [
    CodigoAcessoComponent,
    AutoCadastroComponent,
    SucessoCadastroComponent,
    ChildrenComponent,
    LoginComponent,
    ErrorComponent,
    ProfessionalComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    NgxMaskModule.forRoot()
  ],
  providers: [
    ValidCodeGuard
  ]
})
export class AuthModule { }





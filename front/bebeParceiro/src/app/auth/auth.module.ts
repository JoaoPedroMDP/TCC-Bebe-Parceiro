import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxMaskModule } from 'ngx-mask';
import { PageNotFoundComponent, CodigoAcessoComponent, AutoCadastroComponent, SucessoCadastroComponent } from './index';



@NgModule({
  declarations: [
    CodigoAcessoComponent,
    PageNotFoundComponent,
    AutoCadastroComponent,
    SucessoCadastroComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    NgxMaskModule.forRoot()
  ],
  providers: []
})
export class AuthModule { }





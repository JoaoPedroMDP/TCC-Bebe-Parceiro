import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { PageNotFoundComponent, CodigoAcessoComponent } from './index';
import { AutoCadastroComponent } from './auto-cadastro/auto-cadastro.component';
import { SucessoCadastroComponent } from './sucesso-cadastro/sucesso-cadastro.component';


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
    RouterModule
  ],
  providers: []
})
export class AuthModule { }





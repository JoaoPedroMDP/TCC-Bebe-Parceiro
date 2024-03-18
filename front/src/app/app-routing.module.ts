import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AutoCadastroComponent, CodigoAcessoComponent, LoginComponent, PageNotFoundComponent, SucessoCadastroComponent, ValidCodeGuard } from './auth';

const routes: Routes = [
  // No futuro fazer cada modulo ter seu routing separado assim como é no module e atualizar tudo aqui
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'autocadastro', component: CodigoAcessoComponent},
  { path: 'autocadastro/dados/:codigoAcesso', component: AutoCadastroComponent, canActivate: [ValidCodeGuard]},
  { path: '**', pathMatch: 'full', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

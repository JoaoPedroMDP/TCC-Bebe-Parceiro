import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CodigoAcessoComponent, PageNotFoundComponent } from './auth';

const routes: Routes = [
  // No futuro fazer cada modulo ter seu routing separado assim como é no module e atualizar tudo aqui
  { path: '', redirectTo: 'autocadastro-temp', pathMatch: 'full' },
  { path: 'autocadastro-temp', component: CodigoAcessoComponent},
  { path: '**', pathMatch: 'full', component: PageNotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable, catchError, map } from 'rxjs';
import { AuthService } from '../index';
import { SwalFacade } from 'src/app/shared';
import { HttpResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class ValidCodeGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) { }

  /**
   * @description Guard para verificar se o código de acesso inserido na URL é válido
   * @returns boolean informando se o código foi validado ou não
   */
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {

    const codigoAcesso = route.params['codigoAcesso'];

    return this.authService.sendCode(codigoAcesso).pipe(
      map((response: HttpResponse<any>) => {
        // Aqui você pode acessar o status da resposta
        if (response.status === 200) {
          // Se o status for 200
          return true;
        } else {
          // Se o corpo da resposta estiver vazio ou o status não for 200
          this.router.navigate(['/autocadastro']);
          return false;
        }
      }),
      catchError((err) => {
        // Tratamento de erro 
        this.router.navigate(['/autocadastro']);
        SwalFacade.error('Código Inválido', 'Entre em contato com uma voluntária');
        // Retorno de um Observable false
        return [false];
      })
    );
  }

}

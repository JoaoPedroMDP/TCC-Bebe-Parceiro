import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../services/auth.service';
import { SwalFacade } from 'src/app/shared';

@Injectable({
  providedIn: 'root'
})
export class VolunteerPermisionsGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) { }

  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {

    // Obtém os dados do usuário do serviço de autenticação
    const user = this.authService.getUser();

    // Verifica se o usuário está autenticado
    if (!user) {
      // Redireciona para a página de login se o usuário não estiver autenticado
      this.router.navigate(['/login']);
      SwalFacade.alert("Acesso não autorizado", "Entre no sistema para poder acessar");
      return false;
    }

    // Obtém as permissões necessárias da rota
    const requiredPermissions = next.data['requiredPermissions'] as string[];

    // Verifica se o usuário possui todas as permissões necessárias
    const hasPermission = requiredPermissions.every(permission =>
      user.user?.groups?.some(group =>
        group.name === permission || (group.permissions?.some(p => p.name === permission))));

    // Se o usuário não tiver todas as permissões necessárias, redireciona para a página de acesso não autorizado
    if (!hasPermission) {
      this.router.navigate(['/unauthorized']);
      SwalFacade.alert("Acesso não autorizado", "Você não possui permissões suficientes");
      return false;
    }

    // Permite o acesso à rota se todas as condições forem atendidas
    return true;
  }

}

import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { SwalFacade } from 'src/app/shared';


@Injectable({
  providedIn: 'root',
})
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) { }

  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): boolean {

    const user = this.authService.getUser();

    if (!user) {
      // Usuário não está autenticado
      this.router.navigate(['/login']);
      SwalFacade.alert("Acesso não autorizado", "Entre no sistema para poder acessar");
      return false;
    }

    // Verificar se a role do usuário permite acessar a rota
    const expectedRoles = next.data['expectedRole'];
    const userRole = user.user?.role;

    if (!expectedRoles.includes(userRole)) {
      // Role não corresponde, redirecionar para a página de não
      this.router.navigate(['/unauthorized']);
      return false;
    }

    return true;
  }
}

import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';


@Injectable({
  providedIn: 'root'
})
export class LoginRedirectGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) {}

  canActivate(): boolean {
    const user = this.authService.getUser();
    if (user) {
      this.redirectUserBasedOnRole(user.user?.role);
      return false; // Impede o acesso à rota de login
    }
    return true; // Permite o acesso se não estiver logado
  }

  private redirectUserBasedOnRole(role?: string) {
    switch (role) {
      case 'volunteer':
        this.router.navigate(['/volunteer']);
        break;
      case 'admin':
        this.router.navigate(['/admin']);
        break;
      case 'beneficiary':
        this.router.navigate(['/beneficiada']);
        break;
      default:
        this.router.navigate(['/unauthorized']);
        break;
    }
  }
}

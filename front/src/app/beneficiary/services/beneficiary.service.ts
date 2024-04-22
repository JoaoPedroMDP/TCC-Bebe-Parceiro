import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BeneficiaryService {

  private baseURL!: string;

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL;
  }

  /**
   * @description Faz um DELETE para obter excluir uma beneficiada
   * @param id o Id da beneficiada a ser excluída
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  deleteBeneficiary(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}beneficiaries/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
  
  /**
   * @description Faz um GET para pegar os dados de uma beneficiada especifica
   * @param id id da beneficiada
   * @returns Um Observable contendo os dados de sucesso ou falha
   */
  findBeneficiary(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}beneficiaries/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`${error.status} - ${error.error.message}`));
        })
      );
  }
}

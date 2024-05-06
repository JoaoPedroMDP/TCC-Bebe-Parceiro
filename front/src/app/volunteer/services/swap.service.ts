import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, Subject, catchError, tap, throwError } from 'rxjs';
import { AuthService } from 'src/app/auth';
import { Swap } from 'src/app/shared/models/swap/swap.model';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SwapService {

  private baseURL!: string;
  _refreshPage$ = new Subject<void>();

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL + 'swaps/'; // Supondo que a URL base termine com '/'
  }

  get refreshPage$() {
    return this._refreshPage$;
  }

  createSwap(swap: Swap): Observable<any> {
    return this.http.post(this.baseURL, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  deleteSwap(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  editSwap(id: number, swap: Swap): Observable<any> {
    return this.http.patch(`${this.baseURL}${id}`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  findSwap(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  listSwaps(): Observable<any> {
    return this.http.get(this.baseURL, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }
}

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
  // O Subject irá emitir um valor quando um valor novo for publicado.
  _refreshPage$ = new Subject<void>();

  constructor(private http: HttpClient, private authService: AuthService) {
    this.baseURL = environment.baseURL;
  }


  get refreshPage$() {
    return this._refreshPage$;
  }

  

  createSwap(swap: Swap): Observable<any> {
    return this.http.post(`${this.baseURL}swaps`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  deleteSwap(id: number): Observable<any> {
    return this.http.delete(`${this.baseURL}swaps/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  editSwap(id: number, swap: Swap): Observable<any> {
    return this.http.patch(`${this.baseURL}swaps/${id}`, swap, { headers: this.authService.getHeaders() })
      .pipe(
        tap(() => this._refreshPage$.next()),
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  findSwap(id: number): Observable<any> {
    return this.http.get(`${this.baseURL}swaps/${id}`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }

  listSwaps(): Observable<any> {
    return this.http.get(`${this.baseURL}swaps`, { headers: this.authService.getHeaders() })
      .pipe(
        catchError(error => {
          return throwError(() => new Error(`HTTP error ${error.status}: ${error.error.message}`));
        })
      );
  }
}

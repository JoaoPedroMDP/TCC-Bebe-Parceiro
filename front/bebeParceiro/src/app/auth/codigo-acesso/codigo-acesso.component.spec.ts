import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CodigoAcessoComponent } from './codigo-acesso.component';

describe('CodigoAcessoComponent', () => {
  let component: CodigoAcessoComponent;
  let fixture: ComponentFixture<CodigoAcessoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CodigoAcessoComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CodigoAcessoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

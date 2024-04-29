import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SucessoCadastroComponent } from './sucesso-cadastro.component';

describe('SucessoCadastroComponent', () => {
  let component: SucessoCadastroComponent;
  let fixture: ComponentFixture<SucessoCadastroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SucessoCadastroComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SucessoCadastroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

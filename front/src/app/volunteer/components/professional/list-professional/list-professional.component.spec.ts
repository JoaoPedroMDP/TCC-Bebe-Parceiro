import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListProfessionalComponent } from './list-professional.component';

describe('ListProfessionalComponent', () => {
  let component: ListProfessionalComponent;
  let fixture: ComponentFixture<ListProfessionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListProfessionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListProfessionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
